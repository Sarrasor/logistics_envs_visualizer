<template>
    <div id="map-viewport" class="h-screen">
        <l-map @ready="onReady" ref="map" :zoom="zoom" :center="center" style="z-index: 0;" :use-global-leaflet="false">
            <l-tile-layer :url="url" layer-type="base" name="OpenStreetMap"></l-tile-layer>
            <span v-for="point in points" :key="point.id">
                <l-circle-marker :lat-lng="locationToList(point)" :radius="5" color="#6366f1" :stroke="false"
                    :fillOpacity="0.5">
                </l-circle-marker>
            </span>
        </l-map>
    </div>
</template>

<script setup lang="ts">
import { ref } from "vue"

import {
    LMap,
    LCircleMarker,
    LTileLayer,
} from "@vue-leaflet/vue-leaflet"
import "leaflet/dist/leaflet.css"
import { locationToList } from "../utils/common"

const props = defineProps({
    points: {
        type: Object,
        required: true
    }
})

const map = ref(null)
const zoom = ref(12)
const center = ref([0.0, 0.0])
const url = ref("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png")


function onReady() {
    const average = array => array.reduce((a, b) => a + b) / array.length
    const centerLat = average(props.points.map(point => point.lat))
    const centerLng = average(props.points.map(point => point.lon))
    map.value.leafletObject.panTo({ "lat": centerLat, "lng": centerLng })
}

</script>