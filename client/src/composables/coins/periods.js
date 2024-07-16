export default function usePeriodsList() {
    return {
          selected: null,
          periods: [
              {value: null, text: 'Выбрать период'},
              {value: 1, text: '1 час'},
              {value: 6, text: '6 часов'},
              {value: 12, text: '12 часов'},
              {value: 24, text: '24 часа'},
          ]
      }
}