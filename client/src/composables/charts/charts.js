import {ref} from "vue";
import axios from "axios";

export default function useGraphs() {
    const coinData = ref()
    const chart = ref({})
    /* coin = выбор монеты
       period = период выборки в часах
     */
    const getGraphsData = async (coin = 'POPCATUSDT', period = 1) => {
        let resp = await axios.get("http://127.0.0.1:5000/api/core/coin/" + coin + "/" + period)

        coinData.value = resp.data


        chart.value = {
            current_trend: coinData.value.current_trend,
            options: {
                chart: {
                    type: 'line'
                },
                title: {
                    text: coin
                },
                xAxis: {
                    categories: coinData.value.timestamps
                },
                yAxis: {
                    title: {
                        text: 'Стоимость (USDT)'
                    },
                },
                series: [
                    {
                        name: coin,
                        data: coinData.value.kline_data
                    }
                ]
            }
        }
    }

    console.log(chart)

    return {
        coinData,
        chart,
        getGraphsData
    }
}