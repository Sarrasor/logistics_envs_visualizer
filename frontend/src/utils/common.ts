type Location = { lat: number, lon: number }

type WorkerObservation = { id: string, location: Location }

type Metric = { name: string, value: number, unit: string }

function locationToList(location: Location) {
    return [location.lat, location.lon]
}

function isBright(color: string) {
    color = hexToRgb(color)
    const luminance = (0.299 * color.r + 0.587 * color.g + 0.114 * color.b) / 255.0
    return luminance > 0.5
}

function hexToRgb(hex: string) {
    var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    return result ? {
        r: parseInt(result[1], 16),
        g: parseInt(result[2], 16),
        b: parseInt(result[3], 16)
    } : null;
}

function formatDateTime(dateTime: string) {
    var d = new Date(dateTime)
    return formatDate(dateTime) + ' ' + d.getHours() + ':' + d.getMinutes()
}

function formatDate(dateTime: string) {
    var d = new Date(dateTime),
        month = '' + (d.getMonth() + 1),
        day = '' + d.getDate(),
        year = d.getFullYear()

    if (month.length < 2)
        month = '0' + month
    if (day.length < 2)
        day = '0' + day

    return [day, month, year].join('.')
}

function getMetricValueString(metric: Metric) {
    var value_string = ""
    if (metric.value % 1 != 0) {
        value_string += metric.value.toFixed(2)
    }
    else {
        value_string += metric.value
    }
    if (metric.unit != "%") {
        value_string += " "
    }
    value_string += metric.unit
    return value_string
}

export { locationToList, isBright, formatDateTime, formatDate, getMetricValueString }
export type { Location, WorkerObservation, Metric }