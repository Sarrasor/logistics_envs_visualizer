<template>
    <div>


        <div class="flex items-center justify-center w-full" @change="handleChange" @dragover="dragOverHandler"
            @drop="dropFileHandler">
            <label
                class="flex flex-col items-center justify-center w-full h-64 border-2 border-dashed rounded-lg cursor-pointer dark:hover:bg-bray-800 hover:bg-gray-100 dark:hover:border-gray-500 dark:hover:bg-gray-600"
                :class="getFormStyle(isValid)">
                <div class="flex flex-col items-center justify-center pt-5 pb-6">
                    <div v-if="!model" class="flex flex-col items-center justify-center pt-5 pb-6">
                        <svg class="w-8 h-8 mb-4 text-gray-500 dark:text-gray-400" aria-hidden="true"
                            xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1"
                                d="M10 3v4a1 1 0 0 1-1 1H5m8-2h3m-3 3h3m-4 3v6m4-3H8M19 4v16a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V7.914a1 1 0 0 1 .293-.707l3.914-3.914A1 1 0 0 1 9.914 3H18a1 1 0 0 1 1 1ZM8 12v6h8v-6H8Z" />
                        </svg>

                        <div v-if="!isValid" class="text-red-500">
                            Please provide the input file
                        </div>
                        <p class="mb-2 text-sm text-gray-500 dark:text-gray-400"><span class="font-semibold">Click
                                to
                                upload</span>
                            or drag and drop</p>
                        <p class="text-xs text-gray-500 dark:text-gray-400">.XLS or .XLSX file extensions are
                            supported
                        </p>
                        <RouterLink to="/api/example_file" target="_blank"
                            class="underline block text-center mt-1 text-gray-500 font-bold hover:text-primary-600 dark:text-gray-400">
                            Example problem
                            file
                        </RouterLink>
                    </div>
                    <div v-else class="flex flex-col items-center">
                        <svg class="w-8 h-8 mb-1 text-gray-500 dark:text-gray-400" aria-hidden="true"
                            xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1"
                                d="M8.5 11.5 11 14l4-4m6 2a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
                        </svg>
                        <p class="mb-2 text-base text-gray-500 dark:text-gray-400">File: {{ dropZoneText }}</p>
                    </div>
                </div>
                <input :multiple="multiple" type="file" accept=".xlsx, .xls" class="hidden">
            </label>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { isArray } from 'lodash-es'

interface FileInputProps {
    label?: string
    modelValue?: File | File[] | null
    multiple?: boolean
    size?: string
}

const props = withDefaults(defineProps<FileInputProps>(), {
    label: '',
    modelValue: null,
    multiple: false,
    size: 'sm',
})

const isValid = ref(true)

const dropZoneText = computed(() => {
    if (isArray(props.modelValue)) {
        return props.modelValue.map((el) => el.name).join(', ')
    } else if (props.modelValue instanceof FileList) {
        return Array.from(props.modelValue)
            .map((el) => el.name)
            .join(',')
    } else if (props.modelValue instanceof File) {
        return props.modelValue.name || ''
    }

    return ''
})

const emit = defineEmits(['update:modelValue'])
const model = computed({
    get() {
        return props.modelValue
    },
    set(val) {
        emit('update:modelValue', val)
    },
})

const handleChange = (event: Event) => {
    const target = event.target as HTMLInputElement
    if (props.multiple) {
        model.value = Array.from(target.files ?? [])
    } else {
        model.value = target.files?.[0] ?? null
    }
    isValid.value = true
}

const dropFileHandler = (event: DragEvent) => {
    event.preventDefault()
    const arr: File[] = []
    if (event.dataTransfer?.items) {
        Object.values(event.dataTransfer.items).forEach((item: DataTransferItem) => {
            if (item.kind === 'file') {
                arr.push(item.getAsFile() as File)
            }
        })
        if (props.multiple) {
            model.value = arr
        } else {
            model.value = arr[0]
        }
    } else if (event.dataTransfer?.files) {
        Object.values(event.dataTransfer.files).forEach((file: File) => {
            model.value = file
        })
    }
}

const dragOverHandler = (event: Event) => {
    event.preventDefault()
}

function getFormStyle(valid: boolean) {
    if (valid) {
        return ["bg-white", "border-gray-300", "dark:bg-gray-700", "dark:border-gray-600"]
    }
    else {
        return ["bg-red-100", "border-red-500", "dark:bg-gray-700", "dark:border-red-500"]
    }
}

const invalidateForm = () => {
    isValid.value = false
}

defineExpose({
    invalidateForm
})
</script>