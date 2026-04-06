import matplotlib.pyplot as plt

def generate_pie_chart():
    labels =['Python', 'JavaScript', 'Java', 'C++', 'Ruby']
    values = [30, 25, 20, 15, 10]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%')

    plt.savefig('pie_chart.png')
    plt.close()

