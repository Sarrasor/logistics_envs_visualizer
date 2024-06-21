<template>
    <section
        class="bg-primary-900 dark:bg-very-dark-gray-100 bg-[url('/network.jpg')] bg-no-repeat bg-cover bg-blend-multiply">
        <div class="min-h-screen px-4 mx-auto max-w-screen-lg text-center">
            <h1 class="mb-4 text-[90px] font-black tracking-tight leading-none text-white pt-80">
                Improve your logistics with the power of Reinforcement Learning</h1>
            <p class="mb-8 text-lg font-normal text-gray-200 lg:text-xl sm:px-16 lg:px-48">
                Does not matter whether it is a
                ride-hailing service, a next day delivery service, or a Q-commerce platform
            </p>
            <div class="flex flex-col space-y-4 sm:flex-row sm:justify-center sm:space-y-0">
                <RouterLink to="/solve"
                    class="inline-flex justify-center items-center py-3 px-5 text-base font-medium text-center text-white rounded-lg bg-primary-500 hover:bg-primary-600 focus:ring-4 focus:ring-primary-300 dark:focus:ring-primary-900">
                    Solve my problem
                    <svg class="w-3.5 h-3.5 ms-2 rtl:rotate-180" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
                        fill="none" viewBox="0 0 14 10">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M1 5h12m0 0L9 1m4 4L9 9" />
                    </svg>
                </RouterLink>
                <a href="#how-it-works"
                    class="inline-flex justify-center hover:text-gray-900 items-center py-3 px-5 sm:ms-4 text-base font-medium text-center text-white rounded-lg border border-white hover:bg-gray-100 focus:ring-4 focus:ring-gray-400">
                    Learn more
                </a>
            </div>
        </div>
    </section>

    <div class="text-center py-16 text-black text-7xl font-normal" id="how-it-works">
        How it works
    </div>

    <div class="dark:text-white mb-16 max-w-3xl bg-neutral-100 rounded-2xl p-10 ms-14 shadow-2xl">
        <h2 class="text-xl font-semibold mb-2">Configure</h2>
        <p class=" text-base font-light">Select a logistics environment, load your data as an Excel spreadsheet or enter
            it manually from the interface. Then define remaining run parameters and start the simulation</p>
        <img src="/setup.png" class="mx-auto w-3xl mt-10" />
    </div>

    <div class="dark:text-white mb-16 max-w-3xl bg-neutral-100 rounded-2xl p-10 ms-[56.5rem] shadow-2xl">
        <h2 class="text-xl font-semibold mb-2">Visualize</h2>
        <p class=" text-base font-light">Visualize simulations in real time along with live
            worker telemetry and service metrics. If you do not like to wait, a simulation can be launched in
            the background mode faster than real time</p>
        <img src="/visualize.png" class="mx-auto w-3xl mt-10 rounded-lg" />
    </div>

    <div class="dark:text-white mb-16 max-w-3xl bg-neutral-100 rounded-2xl p-10 ms-24 shadow-2xl">
        <h2 class="text-xl font-semibold mb-2">Inspect</h2>
        <p class=" text-base font-light">When a run is finished, inspect run results, metrics, variable
            distributions, get insights into your data and understand the behavior of your system better
        </p>
        <img src="/inspect.png" class="mx-auto w-3xl mt-10" />
    </div>

    <div class="dark:text-white max-w-3xl bg-neutral-100 rounded-2xl p-10 ms-[56.5rem] shadow-2xl">
        <h2 class="text-xl font-semibold mb-2">Compare</h2>
        <p class=" text-base font-light">Compare multiple runs between each other across multiple dimensions
            and see how different distributions impact the results</p>
        <img src="/compare.png" class="mx-auto w-3xl mt-10" />
    </div>

    <div class="min-h-24"></div>
</template>

<script setup lang="ts">
</script>