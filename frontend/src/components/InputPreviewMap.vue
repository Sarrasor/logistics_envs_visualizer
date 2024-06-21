<template>
    <div id="map-viewport" class="h-[65vh]">
        <l-map @ready="onReady" class="dark:filter dark:invert dark:hue-rotate-180 dark:brightness-60 dark:contrast-98"
            ref="map" :zoom="zoom" :center="center" style="z-index: 0;" :use-global-leaflet="false">
            <l-tile-layer :url="url" layer-type="base" name="OpenStreetMap"></l-tile-layer>
            <span v-for="worker in frameData.observation.workers" :key="worker.id">
                <WorkerMarker :worker="worker" />
            </span>
            <span v-for="order in frameData.observation.orders" :key="order.id">
                <OrderMarker :order="order" />
            </span>
            <span v-for="serviceStation in frameData.observation.service_stations" :key="serviceStation.id">
                <ServiceStationMarker :serviceStation="serviceStation" />
            </span>
        </l-map>
    </div>
</template>

<script setup lang="ts">
import { ref, defineExpose } from "vue"

import {
    LMap,
    LTileLayer,
} from "@vue-leaflet/vue-leaflet"
import "leaflet/dist/leaflet.css"

import WorkerMarker from "./WorkerMarker.vue"
import OrderMarker from "./OrderMarker.vue"
import ServiceStationMarker from "./ServiceStationMarker.vue"

const props = defineProps({
    frameData: {
        type: Object,
        required: true
    }
})

const map = ref(LMap)
const zoom = ref(13)
const center = ref([0.0, 0.0])
const padding = ref([50, 50])
const url = ref("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png")

function onReady() {
}

function prepareBounds(bounds) {
    return [[bounds.min.lat, bounds.min.lon], [bounds.max.lat, bounds.max.lon]]
}

const updateData = (bounds) => {
    if (!map.value.leafletObject) {
        return
    }

    map.value.leafletObject.invalidateSize()
    map.value.leafletObject.fitBounds(prepareBounds(bounds), { padding: padding.value })
}

defineExpose({
    updateData
})

</script>