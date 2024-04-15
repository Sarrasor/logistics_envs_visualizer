<template>
    <l-circle-marker v-if="order.status !== 'COMPLETED'" :lat-lng="getOrderLocationByStatus(order)" :radius="4"
        :color="getOrderColorByStatus(order)" :stroke="false" :fillOpacity="0.8">
        <l-popup :content="orderPopup(order)"></l-popup>
    </l-circle-marker>
</template>


<script setup lang="ts">
import {
    LMarker,
    LIcon,
    LPopup,
    LCircleMarker,
} from "@vue-leaflet/vue-leaflet"
import { locationToList } from "../utils/common"

defineProps({
    order: {
        type: Object,
        required: true
    },
})

function getOrderLocationByStatus(order) {
    if (order.status == "CREATED" || order.status == "ASSIGNED" || order.status == "IN_PICKUP") {
        return locationToList(order.from_location)
    }
    else {
        return locationToList(order.to_location)
    }
}

function getOrderColorByStatus(order) {
    if (order.status == "CREATED" || order.status == "ASSIGNED" || order.status == "IN_PICKUP") {
        return "#0000ff"
    }
    else {
        return "#00ff00"
    }
}

function orderPopup(order: Object) {
    return "<h1><b>Order</b></h1><br>" +
        `<b>Id:</b> ${order.id}<br>` +
        `<b>From Location:</b> ${order.from_location.lat.toFixed(6)}, ${order.from_location.lon.toFixed(6)}</br>` +
        `<b>To Location:</b> ${order.to_location.lat.toFixed(6)}, ${order.to_location.lon.toFixed(6)}</br>` +
        `<b>Status:</b> ${order.status}<br>`
}

</script>