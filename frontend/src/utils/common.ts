type Location = { lat: number, lon: number };

type WorkerObservation = { id: string, location: Location };

function locationToList(location: Location) {
    return [location.lat, location.lon]
}

export { locationToList }
export type { Location, WorkerObservation }