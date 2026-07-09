import streamlit as st
import json
from agents.graph import builder
import os

st.set_page_config(
    page_title="LangGraph Playground",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 LangGraph Playground")

st.markdown("---")

tab1, tab2, tab3 = st.tabs([
    "📈 Graph",
    "💻 Source Code",
    "▶ Run Graph"
])

###################################################
# GRAPH TAB
###################################################

with tab1:

    st.header("Graph Visualization")

    png = builder.get_graph().draw_mermaid_png()

    st.image(png, use_container_width=True)

###################################################
# SOURCE CODE TAB
###################################################

with tab2:

    st.header("graph.py")
    import os

    graph_file = os.path.join(
        os.path.dirname(__file__),
        "graph.py"
    )

    with open(graph_file, "r") as f:
        code = f.read()


    st.code(code, language="python")

###################################################
# RUN TAB
###################################################

with tab3:

    st.header("Execute Graph")

    graph_input = st.text_input(
        "Graph Input",
        "My name is Siddhartha"
    )

    if st.button("Run Graph", use_container_width=True):

        st.subheader("Input")

        st.json({
            "graph_info": graph_input
        })

        st.divider()

        st.subheader("Execution Trace")

        placeholder = st.empty()

        trace = []

        for event in builder.stream(
                {"graph_info": graph_input}
        ):
            trace.append(event)
            placeholder.json(trace)

        st.divider()

        result = builder.invoke(
            {"graph_info": graph_input}
        )

        st.subheader("Final Output")

        st.json(result)

