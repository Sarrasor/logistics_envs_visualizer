<template>
    <div ref="plotlyId" name="plotly"></div>
</template>

<script setup lang="ts">
import { ref, onMounted, watchEffect } from 'vue';
import type { Ref } from 'vue'
import Plotly from 'plotly.js-dist-min'

const props = defineProps({
    data: {
        type: Array,
        required: true,
    },
    layout: {
        type: Object,
        required: true,
    },
    config: {
        type: Object,
        required: false,
        default: { responsive: true },
    },
});

const plotlyId: Ref<null | HTMLDivElement> = ref(null);
const ready = ref(false);

function setGraph() {
    if (!ready.value || !plotlyId.value || !props.data || !props.layout) return;
    Plotly.newPlot(plotlyId.value, props.data, props.layout, props.config);
}

onMounted(() => {
    ready.value = true;
    setGraph();
});

watchEffect(() => {
    setGraph();
})
</script>