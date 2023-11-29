import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import os
import warnings

warnings.filterwarnings("ignore")

st.set_page_config(
    page_title="Superstore Dashboard", page_icon=":bar_chart:", layout="wide"
)

st.markdown(
    "<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True
)
st.title(":bar_chart: Superstore Dashboard")

fl = st.file_uploader(":file_folder: Upload a file", type=["csv"])
if fl is not None:
    filename = fl.name
    st.write(f"File uploaded: {filename}")
    df = pd.read_csv(filename, encoding="ISO-8859-1")
else:
    os.chdir(r"C:\Users\NoNm3\Desktop\Streamlit")
    df = pd.read_csv("Superstore.csv", encoding="ISO-8859-1")

col1, col2 = st.columns(2)
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Get min and max date
startDate = pd.to_datetime(df["Order Date"]).min()
endDate = pd.to_datetime(df["Order Date"]).max()

with col1:
    date1 = pd.to_datetime(st.date_input("Start Date", startDate))

with col2:
    date2 = pd.to_datetime(st.date_input("End Date", endDate))

# df = df[(df["Order Date"] >= date1) & (df["Order Date"] <= date2)].copy()
df = df[(df["Order Date"] >= date1) & (df["Order Date"] <= date2)].copy()
if date1 > date2:
    st.error("Error: End date must fall after start date.")
else:
    df = df[(df["Order Date"] >= date1) & (df["Order Date"] <= date2)].copy()

st.sidebar.title(":mag: Filters")

# Region filter
region = st.sidebar.multiselect("Pick the Region", df["Region"].unique())
if not region:
    df2 = df.copy()
else:
    df2 = df[df["Region"].isin(region)]

# State filter
state = st.sidebar.multiselect("Pick the State", df2["State"].unique())
if not state:
    df3 = df2.copy()
else:
    df3 = df2[df2["State"].isin(state)]

city = st.sidebar.multiselect("Pick the City", df3["City"].unique())


# Check if no filters are selected
if not region and not state and not city:
    filtered_df = df
else:
    # Initialize a boolean mask with True values
    mask = pd.Series(True, index=df.index)

    # Apply filters based on selected criteria
    if region:
        mask &= df["Region"].isin(region)
    if state:
        mask &= df["State"].isin(state)
    if city:
        mask &= df["City"].isin(city)

    # Apply the combined filter to the DataFrame
    filtered_df = df[mask]

category_df = filtered_df.groupby(by=["Category"], as_index=False)["Sales"].sum()

with col1:
    st.subheader(":chart_with_upwards_trend: Category-wise Sales")
    fig = px.bar(
        category_df,
        x="Category",
        y="Sales",
        text=["{:,.2f}".format(x) for x in category_df["Sales"]],
        template="presentation",
        color="Category",
    )
    st.plotly_chart(fig, use_container_width=True, height=200)

with col2:
    st.subheader(":chart_with_upwards_trend: Region-wise Sales")
    fig = px.pie(
        filtered_df,
        values="Sales",
        names="Region",
        hole=0.4,
    )
    fig.update_traces(text=filtered_df["Region"], textposition="outside")
    st.plotly_chart(fig, use_container_width=True)

cl1, cl2 = st.columns(2)
with cl1:
    with st.expander("Category_Viewdata"):
        st.write(category_df.style.background_gradient(cmap="Blues"))
        csv = category_df.to_csv(index=False).encode("utf-8")
        st.download_button(
            "Download Data",
            data=csv,
            file_name="Category.csv",
            mime="text/csv",
            help="Click here to download the data as a CSV file",
        )

with cl2:
    with st.expander("Region_Viewdata"):
        region = filtered_df.groupby(by="Region", as_index=False)["Sales"].sum()
        st.write(region.style.background_gradient(cmap="Oranges"))
        csv = region.to_csv(index=False).encode("utf-8")
        st.download_button(
            "Download Data",
            data=csv,
            file_name="Region.csv",
            mime="text/csv",
            help="Click here to download the data as a CSV file",
        )

filtered_df["month_year"] = filtered_df["Order Date"].dt.to_period("M")
st.subheader("Time Series Analysis")
linechart = pd.DataFrame(
    filtered_df.groupby(filtered_df["month_year"].dt.strftime("%Y : %b"))["Sales"].sum()
).reset_index()
fig2 = px.line(
    linechart,
    x="month_year",
    y="Sales",
    labels={"Sales": "Amount"},
    height=500,
    width=1000,
    template="presentation",
)
st.plotly_chart(fig2, use_container_width=True)

with st.expander("View Data as TimeSeries:"):
    st.write(linechart.T.style.background_gradient(cmap="Blues"))
    csv = linechart.to_csv(index=False).encode("utf-8")
    st.download_button(
        "Download Data", data=csv, file_name="TimeSeries.csv", mime="text/csv"
    )

st.subheader("Hierarchical Sales Using Treemap")
fig3 = px.treemap(
    filtered_df,
    path=["Region", "Category", "Sub-Category"],
    values="Sales",
    color="Sales",
    hover_data=["Sales"],
    color_continuous_scale="RdBu",
    title="Hierarchical Sales Using Treemap",
)
fig.update_layout(margin=dict(l=20, r=20, t=30, b=20))
st.plotly_chart(fig3, use_container_width=True)
