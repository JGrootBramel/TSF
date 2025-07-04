import matplotlib.pyplot as plt

def plot_series(df):

    fig, ax = plt.subplots()

    ax.plot(df.date, df.data)
    ax.set_xlabel('Date')
    ax.set_ylabel('Earnings per share (USD)')

    fig.autofmt_xdate()
    plt.tight_layout()