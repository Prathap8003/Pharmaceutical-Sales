import streamlit as st
import pandas as pd
import plotly.express as px


@st.cache_data
def load_data():
    return pd.read_csv('salesdaily.csv')

def show_interpretation():
    st.header('Interpretation')
    st.write("The pharmaceutical sales dashboard provides users with a comprehensive overview of sales data spanning six years, from 2014 to 2019. Through this application, users can analyze and extract insights from the dataset, focusing on specific drug categories to understand sales trends and patterns effectively.\n")
    st.write("1. **Pharmaceutical Sales Dataset Overview**: This section offers users a succinct summary of the dataset, highlighting key information such as the duration of data collection and the inclusion of various ATC drug categories. It serves as a foundational understanding of the dataset's scope and contents.\n")
    st.write("2. **Select Drug Category**: Users are empowered to narrow down their analysis by selecting a specific drug category from the provided dropdown menu. This feature allows users to tailor their exploration to focus on areas of interest within the pharmaceutical market.\n")
    st.write("3. **Visualizations**: The application generates several visualizations based on the selected drug category, each offering unique insights into sales dynamics:\n")
    st.write("   - **Sales Trend Histogram**: Provides a visual representation of the sales trend over time for the chosen drug category, facilitating the identification of recurring patterns and fluctuations.\n")
    st.write("   - **Sales Scatter Plot**: Illustrates the relationship between sales and date, enabling users to detect correlations or anomalies in sales data over time.\n")
    st.write("   - **Monthly Sales Distribution Box Plot**: Presents the distribution of sales across different months, aiding in understanding the variability of sales performance throughout the year.\n")
    st.write("   - **Exact Frequency and Highest Sales per Month**: Delivers precise information on sales frequency and the highest recorded sales within each month, offering valuable insights into sales performance metrics.\n")
    st.write("   - **Raw Data Display**: Enables users to explore the underlying dataset, facilitating further analysis and investigation beyond the provided visualizations.\n")
    st.write("\nIn summary, this pharmaceutical sales dashboard equips users with the tools to conduct in-depth analysis and derive actionable insights from the sales dataset. By enabling users to explore specific drug categories and visualize sales trends, the application supports informed decision-making processes within the pharmaceutical industry. Furthermore, it lays the groundwork for future enhancements, such as incorporating advanced analytics and interpretation features to deepen understanding and extract additional value from the data.")

def show_dataset_overview():
    st.header('Pharmaceutical Sales Dataset Overview')
    st.write("The dataset contains pharmaceutical sales data collected over a 6-year period (2014-2019).")
    st.write("The dataset includes the following ATC drug categories:")
    st.write("- M01AB: Anti-inflammatory and antirheumatic products, non-steroids (Acetic acid derivatives and related substances)")
    st.write("- M01AE: Anti-inflammatory and antirheumatic products, non-steroids (Propionic acid derivatives)")
    st.write("- N02BA: Other analgesics and antipyretics (Salicylic acid and derivatives)")
    st.write("- N02BE/B: Other analgesics and antipyretics (Pyrazolones and Anilides)")
    st.write("- N05B: Psycholeptics drugs (Anxiolytic drugs)")
    st.write("- N05C: Psycholeptics drugs (Hypnotics and sedatives drugs)")
    st.write("- R03: Drugs for obstructive airway diseases")
    st.write("- R06: Antihistamines for systemic use")

    

def show_drug_selection():
    st.sidebar.header('Select Drug Category:')
    selected_category = st.sidebar.selectbox('', ['M01AB', 'M01AE', 'N02BA', 'N02BE', 'N05B', 'N05C', 'R03', 'R06'])
    return selected_category

def show_drug_category(selected_category):
    df = pd.read_csv('salesdaily.csv')
    df_monthly = df.groupby('Month')[selected_category].sum().reset_index()

    st.header(f'{selected_category} Sales Trend')
    fig_hist = px.histogram(df_monthly, x=selected_category, title=f'{selected_category} Sales Trend')
    fig_hist.update_xaxes(title_text='Sales')
    fig_hist.update_yaxes(title_text='Frequency')
    st.plotly_chart(fig_hist)

    st.header(f'Sales Scatter Plot for {selected_category}')
    fig_scatter = px.scatter(df, x='datum', y=selected_category, title=f'Sales Scatter Plot for {selected_category}', color=selected_category, color_continuous_scale=[ '#92c5de', '#4393c3', '#2166ac', '#053061'])
    fig_scatter.update_xaxes(title_text='Date')
    fig_scatter.update_yaxes(title_text='Sales')
    st.plotly_chart(fig_scatter)


    st.header(f'Monthly Sales Distribution for {selected_category}')
    fig_box = px.box(df, x='Month', y=selected_category, title=f'Monthly Sales Distribution for {selected_category}')
    fig_box.update_xaxes(title_text='Month')
    fig_box.update_yaxes(title_text='Sales')
    st.plotly_chart(fig_box)

 
    st.header("Exact Frequency and Highest Sales per Month")
    max_sales_month = df_monthly[df_monthly[selected_category] == df_monthly[selected_category].max()]["Month"].values[0]
    max_sales_value = df_monthly[selected_category].max()
    st.write(f"Highest Sales: {max_sales_value} in {max_sales_month}")
    st.write("Frequency of Sales:")
    st.dataframe(df_monthly)  # Changed st.write(df_monthly) to st.dataframe(df_monthly)
    if st.checkbox('Show Raw Data'):
        st.dataframe(df)  # Changed st.write(df) to st.dataframe(df)

def main():
    st.title("Pharmaceutical Sales Dashboard")
    st.sidebar.title('Select Option:')
    selected_option = st.sidebar.selectbox('', ['Pharmaceutical Sales Dataset Overview', 'Select Drug Category', 'Interpretation'])
    print(selected_option)
    if selected_option == 'Pharmaceutical Sales Dataset Overview':
        show_dataset_overview()
    elif selected_option == 'Select Drug Category':
        show_drug_category(show_drug_selection())
    elif selected_option == 'Interpretation':
        show_interpretation()
    else:
        st.error("Invalid selection.")

def show_dashboard():
    df = load_data()
    with st.sidebar:
        st.title('Pharmaceutical Sales Dashboard')
        st.subheader('Select Drug Category:')
        selected_category = st.selectbox('', ['M01AB', 'M01AE', 'N02BA', 'N02BE', 'N05B', 'N05C', 'R03', 'R06'])
        st.subheader('Pharmaceutical Sales Dataset Overview')
        st.write("The dataset contains pharmaceutical sales data collected over a 6-year period (2014-2019).")
        st.write("The dataset includes the following ATC drug categories:")
        st.write("- M01AB: Anti-inflammatory and antirheumatic products, non-steroids (Acetic acid derivatives and related substances)")
        st.write("- M01AE: Anti-inflammatory and antirheumatic products, non-steroids (Propionic acid derivatives)")
        st.write("- N02BA: Other analgesics and antipyretics (Salicylic acid and derivatives)")
        st.write("- N02BE/B: Other analgesics and antipyretics (Pyrazolones and Anilides)")
        st.write("- N05B: Psycholeptics drugs (Anxiolytic drugs)")
        st.write("- N05C: Psycholeptics drugs (Hypnotics and sedatives drugs)")
        st.write("- R03: Drugs for obstructive airway diseases")
        st.write("- R06: Antihistamines for systemic use")
    df_monthly = df.groupby('Month')[selected_category].sum().reset_index()
   
   
    
    st.title("Exact Frequency and Highest Sales per Month")
    max_sales_month = df_monthly[df_monthly[selected_category] == df_monthly[selected_category].max()]["Month"].values[0]
    max_sales_value = df_monthly[selected_category].max()
    st.write(f"Highest Sales: {max_sales_value} in {max_sales_month}")
    st.write("Frequency of Sales:")
    st.write(df_monthly)
    if st.checkbox('Show Raw Data'):
        st.write(df)

if __name__ == '__main__':
    main()

