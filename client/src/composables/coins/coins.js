export default function useCoinList() {
    return {
          selected: null,
          options: [
              {value: null, text: 'Выбрать монету'},
              {value: 'POPCATUSDT', text: 'POPCAT'},
              {value: 'NOTUSDT', text: 'NOT'},
              {value: 'BTCUSDT', text: 'BTC'},
          ]
      }
}