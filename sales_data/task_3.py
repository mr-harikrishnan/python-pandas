from matplotlib import ticker
import pandas as pd
import matplotlib.pyplot as plt


def ordersDataClean(ordersDf):

    ordersDf["order_id"] = ordersDf["order_id"].str.strip().str.upper()

    ordersDf["customer_id"] = ordersDf["customer_id"].str.strip().str.upper()

    ordersDf["order_date"] = ordersDf["order_date"] = pd.to_datetime(
        ordersDf["order_date"], format="mixed", dayfirst=True, errors="coerce"
    )

    ordersDf["product"] = ordersDf["product"].str.strip().str.capitalize()

    return ordersDf


def customersDataClean(customersDf):

    customersDf["customer_id"] = customersDf["customer_id"].str.strip().str.upper()

    customersDf["customer_name"] = customersDf["customer_name"].str.strip().str.title()

    customersDf["city"] = customersDf["city"].str.strip().str.title()

    customersDf["segment"] = customersDf["segment"].str.strip().str.capitalize()

    customersDf["signup_date"] = customersDf["signup_date"] = pd.to_datetime(
        customersDf["signup_date"], format="mixed", dayfirst=True, errors="coerce"
    )

    return customersDf


def addRevenueColumn(orderDf):

    orderDf["revenue"] = orderDf["quantity"] * orderDf["unit_price"]

    return orderDf


def revenueperMonth(orderDf):

    orderDf = orderDf.sort_values("order_date")

    orderDf["month"] = orderDf["order_date"].dt.month_name()

    monthlyRevenue = orderDf.groupby("month", sort=False)["revenue"].sum()

    chartData = monthlyRevenue.head(6)

    plt.figure(figsize=(8, 5))

    plt.plot(chartData.index, chartData.values, marker="o", color="grey", alpha=0.6)

    for i in range(len(chartData)):

        x = chartData.index[i]

        y = chartData.iloc[i]

        plt.text(
            x,
            y,
            f"{int(y):,}",
            ha="center",
            fontsize=8,
        )

    plt.title("Revenue Per Month (January - June)")
    plt.grid()
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.show()


def totalRevenueByProduct(orderDf):

    revenueByProduct = orderDf.groupby("product")["revenue"].sum()

    revenueByProductChart = pd.DataFrame(
        {"product": revenueByProduct.index, "revenue": revenueByProduct.values}
    )

    revenueByProductChartData = revenueByProductChart.sort_values(
        "revenue", ascending=False
    )

    totalRevenue = revenueByProductChart["revenue"].sum()

    highestRevenue = revenueByProductChartData.iloc[0]["revenue"]

    topProduct = revenueByProductChartData.iloc[0]["product"]

    print(highestRevenue, totalRevenue, topProduct)

    print(revenueByProductChartData)

    percentage = (highestRevenue / totalRevenue) * 100

    print(
        f"Highest revenue product {topProduct} contributes {percentage:.2f}% of total revenue"
    )

    plt.figure(figsize=[12, 6])

    bars = plt.bar(
        revenueByProductChartData["product"], revenueByProductChartData["revenue"]
    )

    for bar in bars:
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            f"{int(bar.get_height()):,}",
            ha="center",
            va="bottom",
            fontsize=8,
        )

    plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter("{x:,.0f}"))

    plt.grid(alpha=0.3)

    plt.xlabel("Product Names")

    plt.ylabel("Revenue details")

    plt.title("Total Revenue by Product")

    plt.figtext(
        0.5,
        0.01,
        f"Highest revenue product {topProduct} contributes {percentage:.2f}% of total revenue",
        ha="center",
        fontsize=10,
    )

    plt.show()


def cityRevenueAndOrders(ordersDf, customerDf):

    mergedData = ordersDf.merge(customerDf)

    citesWithRevenue = (
        mergedData.groupby("city")["revenue"].sum().sort_values(ascending=False)
    )

    citiesWithOrderCount = (
        mergedData.groupby("city")["order_id"].nunique().sort_values(ascending=False)
    )
    print(citesWithRevenue)

    print(citiesWithOrderCount)

    fig, ax = plt.subplots(1, 2, figsize=(14, 6))

    # citesWithRevenue
    bars1 = ax[0].bar(citesWithRevenue.index, citesWithRevenue.values)

    ax[0].set_title("Cities Ranked by Total Revenue")
    ax[0].set_xlabel("City")
    ax[0].set_ylabel("Total Revenue")

    for bar in bars1:
        ax[0].text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            f"{int(bar.get_height()):,}",
            ha="center",
            va="bottom",
            fontsize=8,
        )

    # citiesWithOrderCount

    bars2 = ax[1].bar(citiesWithOrderCount.index, citiesWithOrderCount.values)

    ax[1].set_title("Cities Ranked by Number of Orders")
    ax[1].set_xlabel("City")
    ax[1].set_ylabel("Number of Orders")

    for bar in bars2:
        ax[1].text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            f"{int(bar.get_height())}",
            ha="center",
            va="bottom",
            fontsize=8,
        )

    plt.show()


def main():

    ordersDf = pd.read_csv("./orders.csv")

    customerDf = pd.read_csv("./customers.csv")

    # DATA-CLEAN

    ordersDf = ordersDataClean(ordersDf)

    customerDf = customersDataClean(customerDf)

    # 1.⁠ ⁠Line chart: revenue per month, January → June.
    # The months must appear in calendar order.
    # (Careful — pandas has an opinion about ordering that you've met before.)

    ordersDf = addRevenueColumn(ordersDf)

    # revenueperMonth(ordersDf)

    # 2.⁠ ⁠Bar chart: total revenue by product, sorted so the biggest bar is instantly visible.
    # Add one sentence below the chart: what % of total revenue is the top product? (Compute it, don't eyeball it.)

    # totalRevenueByProduct(ordersDf)

    # 3.⁠ ⁠Two bar charts side by side (plt.subplots(1, 2)): cities ranked by total revenue,
    # and cities ranked by number of orders. Look at both. Write 2–3 sentences: what contradiction do you see,
    # and which city would you call "best"?

    cityRevenueAndOrders(ordersDf, customerDf)


main()
