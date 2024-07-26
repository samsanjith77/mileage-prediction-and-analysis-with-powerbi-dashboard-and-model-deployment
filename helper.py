import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
cars=pd.read_csv('chart.csv')


# chart for avg mpg according to the country
def avg_country(org):
    f = cars.groupby(['country', 'model_year'])['mpg'].mean().reset_index()
    data = f.loc[f['country'] == org][['model_year', 'mpg']]
    fig, ax = plt.subplots()
    ax.bar(x=data['model_year'], height=data['mpg'])
    ax.set_title(f'AVG of mpg in {org}')
    ax.set_xlabel('Model Year')
    ax.set_ylabel('Average MPG')
    return fig
def cylinder_mpg():
    plt.figure(figsize=(7,7))
    sns.scatterplot(data=cars,x='cylinders',y='mpg')
    plt.title("MPG over cylinder")
    plt.tight_layout()
    return plt.gcf()
def company_car():
    plt.figure(figsize=(7,7))
    sns.countplot(data=cars,x='company')
    plt.xticks(rotation=60)
    plt.tight_layout()
    return plt.gcf()
