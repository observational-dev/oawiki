/**
 * Preprocess the data from ernests_list.json, which itself is scraped from
 * Ernest's list of eyepiece stats/measuremens from astro-talks.ru.
 *
 * @param {any} data Array of objects containing entries for the eyepiecees table.
 * @returns Array<any> A cleaned array with simple keys and values to display.
 */
function process(data) {
  return data.map((item) => {
    // This pattern searches for values of the form
    //   82.1(79.3)
    //   81
    //   19(19.2)
    // And splits them apart into two pieces - the nominal and measured values.
    const pattern = /(?<nominal>\d+(\.\d+)?)(\((?<measured>\d+\.\d+)\))?/

    // Extract out number in parenthesis of focal length; this is the measured FL
    const flMatch = item['FL [mm]'].match(pattern)
    // Extract out number in parenthesis of calculated AFOV; this is calculated
    // from the measured FL rather than the manufacturer's nominal FL
    const afovMatch = item["2w' [°]"].match(pattern)

    return {
      eyepiece: item['Eyepiece'],
      focalLengthNominal: flMatch?.groups?.nominal ?? item['FL [mm]'],
      focalLengthMeasured: flMatch?.groups?.measured ?? '',
      fieldStop: item['2Y [mm]'],
      nominalCalculatedAFOV: afovMatch?.groups?.nominal ?? item["2w' [°]"],
      measuredCalculatedAFOV: afovMatch?.groups?.measured ?? '',
      measuredAFOV: item['AFOV [°]'],
      f4axis: item['F4 axis'],
      f4zone: item['F4 zone'],
      f4edge: item['F4 edge'],
      f10axis: item['F10 axis'],
      f10zone: item['F10 zone'],
      f10edge: item['F10 edge'],
      otherAberrations: item['Other aberrations'],
      alsoKnownAs: item['Also known as'],
    }
  })
}

fetch('../../_static/ernests_list.json')
  .then((response) => response.json())
  .then((data) => process(data))
  .then((data) => {
    // eslint-disable-next-line no-undef
    new Tabulator('#grid-wrapper', {
      height: 0.95 * document.querySelector('article.bd-article').offsetHeight,
      data,
      columns: [
        { field: 'eyepiece', title: 'Eyepiece' },
        { field: 'focalLengthNominal', title: 'Nominal FL [mm]' },
        { field: 'focalLengthMeasured', title: 'Measured FL [mm]' },
        { field: 'fieldStop', title: 'Field Stop [mm]' },
        {
          field: 'nominalCalculatedAFOV',
          title: 'Calculated AFOV (Nominal FL) [°]',
        },
        {
          field: 'measuredCalculatedAFOV',
          title: 'Calculated AFOV (Measured FL) [°]',
        },
        { field: 'measuredAFOV', title: 'Measured AFOV [°]' },
        { field: 'f4axis', title: 'F4 Axis' },
        { field: 'f4zone', title: 'F4 Zone' },
        { field: 'f4edge', title: 'F4 Edge' },
        { field: 'f10axis', title: 'F10 Axis' },
        { field: 'f10zone', title: 'F10 Zone' },
        { field: 'f10edge', title: 'F10 Edge' },
        { field: 'otherAberrations', title: 'Other Aberrations' },
        { field: 'alsoKnownAs', title: 'Also Known As' },
      ],
    })
  })
