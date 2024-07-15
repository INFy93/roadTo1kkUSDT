import {ref} from "vue";
import axios from "axios";

export default function useGraphs()
{
    const coinData = ref()
    const chart = ref({})
    const getGraphsData = async (coin='POPCATUSDT') => {
        let resp = await axios.get("http://127.0.0.1:5000/api/core/coin/" + coin)

        coinData.value = resp.data


        chart.value = {
            options: {
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