import streamlit as st

st.set_page_config(
    page_title='Teams',
    page_icon="🏴",
    layout="wide"
)

df_data = st.session_state["data"]

clubes =  df_data["Club"].value_counts().index
club = st.sidebar.selectbox("Clube", clubes)

df_filered = df_data[(df_data["Club"] == club)].set_index("Name")

st.image(df_filered.iloc[0]["Club Logo"])
st.markdown(f"## {club}")

coluns = ["Age", "Photo", "Flag", "Overall", "Value(£)",
          "Wage(£)", "Joined", "Height(cm.)", "Weight(lbs.)",
          "Contract Valid Until", "Release Clause(£)"]

st.dataframe(df_filered[coluns],
             column_config={ 
                 "Overall": st.column_config.ProgressColumn(
                     "Overall", min_value=0, max_value=100
                 ),
                 "Wage(£)": st.column_config.ProgressColumn("Ganho semanal", format="£%f",
                                                            min_value=0, max_value=df_filered["Wage(£)"].max()),
                    "Photo": st.column_config.ImageColumn(),
                    "Flag": st.column_config.ImageColumn("Country"),
             })