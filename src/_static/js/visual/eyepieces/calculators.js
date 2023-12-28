/* eslint-disable no-undef */
function debounce(func, timeout = 300) {
  let timer
  return (...args) => {
    clearTimeout(timer)
    timer = setTimeout(() => func.apply(this, args), timeout)
  }
}

/**
 * Compute any eyepiece properties which depend on user input.
 *
 * @param {any} data Array of objects containing entries for the eyepieces table.
 * @returns Array<any> A cleaned array with simple keys and values to display.
 */
function processEyepieces(data, telescopeFL = NaN, telescopeFR = NaN) {
  return data.map((item) => {
    const magnificationNominal = telescopeFL / item.focalLengthNominal
    return {
      ...item,
      magnificationNominal,
      exitPupilNominal: item.focalLengthNominal / telescopeFR,
      tfovNominal: item.afov / magnificationNominal,
    }
  })
}

/**
 * Rename the columns of the data from ernests_list.json, which itself is scraped from
 * Ernest's list of eyepiece stats/measurements from astro-talks.ru.
 *
 * @param {any} data Array of objects containing entries for the eyepieces table.
 * @returns Array<any> An array with simple keys and values to display.
 */
function processEyepiecesJSON(data) {
  return data.map((item) => {
    return {
      brand: item['1 Brand'],
      model: item['Model'],
      manufacturer: item['MFR'],
      category: item['Category'],
      focalLengthNominal: item['FL'],
      diameter: item['Diam.'],
      afov: item['AFOV'],
      weight: item['Wt.'],
      eyeRelief: item['Eye Relief'],
      fieldStopNominal: item["Mfr's Field Stop "],
      fieldStopCalculated: item['Calc.FieldStop'],
      undercuts: item['Undercuts?'],
      coatings: item['Coatings'],
      blackenedEdge: item['Edge black'],
      nElements: item['Elem.'],
      magnificationNominal: NaN,
      exitPupilNominal: NaN,
      tfovNominal: NaN,
    }
  })
}

document.addEventListener('DOMContentLoaded', () => {
  const inputFL = document.getElementById('telescope-focal-length')
  const inputFR = document.getElementById('telescope-focal-ratio')

  inputFL.oninput = debounce(updateUI)
  inputFL.onpaste = inputFL.oninput()

  inputFR.oninput = debounce(updateUI)
  inputFR.onpaste = inputFR.oninput()
})

function updateUI() {
  const inputFL = document.getElementById('telescope-focal-length')
  const inputFR = document.getElementById('telescope-focal-ratio')

  updateTable(inputFL.value, inputFR.value)
}

// eslint-disable-next-line no-undef
const table = new Tabulator('#grid-wrapper', {
  height: 0.95 * document.querySelector('article.bd-article').offsetHeight,
  columns: [
    { field: 'brand', title: 'Brand' },
    { field: 'model', title: 'Model' },
    { field: 'manufacturer', title: 'Manufacturer' },
    { field: 'category', title: 'Category' },
    { field: 'focalLengthNominal', title: 'Nominal FL [mm]' },
    { field: 'diameter', title: 'Barrel Diameter [in]' },
    { field: 'afov', title: 'Nominal AFOV [°]' },
    { field: 'weight', title: 'Weight [g]' },
    { field: 'eyeRelief', title: 'Eye Relief [mm]' },
    { field: 'fieldStopNominal', title: 'Field Stop (Nominal) [mm]' },
    { field: 'fieldStopCalculated', title: 'Field Stop (Calculated) [mm]' },
    { field: 'undercuts', title: 'Undercuts' },
    { field: 'coatings', title: 'Coatings' },
    { field: 'blackenedEdge', title: 'Blackened Edge' },
    { field: 'nElements', title: 'Number of Elements' },
    { field: 'magnificationNominal', title: 'Magnification (Nominal)' },
    { field: 'exitPupilNominal', title: 'Exit Pupil (Nominal) [mm]' },
    { field: 'tfovNominal', title: 'TFOV (Nominal) [°]' },
  ],
})

let tableData = undefined

fetch('../../_static/eyepiece_buyers_guide_fixed.json')
  .then((response) => response.json())
  .then((rawData) => {
    tableData = processEyepiecesJSON(rawData)
    table.setData(tableData)
  })

function updateTable(telescopeFL, telescopeFR) {
  tableData = processEyepieces(
    tableData,
    telescopeFL === '' ? NaN : telescopeFL,
    telescopeFR === '' ? NaN : telescopeFR
  )
  table.replaceData(tableData)
}
