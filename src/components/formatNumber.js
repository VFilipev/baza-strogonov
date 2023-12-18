export const formatNumber = function (value, round = 0) {
  if (value && parseFloat(value)) {
    let parts = parseFloat(value).toFixed(round).toString().split('.')

    parts[0] = parts[0].replace(/\d(?=(\d{3})+$)/g, '$&\xa0')
    if (parts.length == 1 && round != 0) {
      parts.push('00')
    }
    return parts.join(',')
  } else {
    if (value === null) {
      return 0
    } else if (value === undefined || isNaN(value)) {
      return ''
    } else {
      return value
    }
  }
}
