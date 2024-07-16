export default function usePeriodsList() {
    return {
          selected: null,
          options: [
              {value: null, text: 'Выбрать период'},
              {value: 1, text: '1 час'},
              {value: 12, text: '12 часов'},
              {value: 24, text: '24 часа'},
          ]
      }
}