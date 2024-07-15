import {ref} from "vue";
import axios from "axios";

export default function useBalance()
{
    const balance = ref(0)

    const getAviableBalance = async () => {
        let response = await axios.get("http://127.0.0.1:5000/api/account/balance")

        balance.value = parseFloat(response.data)
    }

    return {
        balance,
        getAviableBalance
    }
}