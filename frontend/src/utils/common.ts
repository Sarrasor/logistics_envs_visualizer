type Location = { lat: number, lon: number };

type WorkerObservation = { id: string, location: Location };

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

export { locationToList, isBright }
export type { Location, WorkerObservation }