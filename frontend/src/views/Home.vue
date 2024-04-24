<template>
    <div class="py-8 px-4 mx-auto max-w-screen-xl text-center lg:py-16">
        <img src="/logo.svg" alt="Logviz logo" class="mx-auto w-40" />
        <h1
            class="mb-4 text-4xl font-extrabold tracking-tight leading-none text-gray-900 md:text-5xl lg:text-6xl dark:text-white">
            Logviz
        </h1>
        <p class="mb-8 text-lg font-normal text-gray-500 lg:text-xl sm:px-16 lg:px-48 dark:text-gray-400">
            Visualizer for logistics problems and their solutions
        </p>
        <div class="flex flex-col space-y-4 sm:flex-row sm:justify-center sm:space-y-0">
            <div class="flex flex-col space-y-4 sm:flex-row sm:justify-center sm:space-y-0">
                <RouterLink to="/solve"
                    class="inline-flex text-white bg-primary-400 hover:bg-primary-500 focus:ring-4 focus:outline-none focus:ring-primary-300 font-bold rounded-lg text-xl px-10 py-5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800 my-4">
                    Solve my problem
                </RouterLink>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
</script>