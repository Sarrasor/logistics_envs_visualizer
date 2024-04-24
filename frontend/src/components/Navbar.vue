<template>
    <nav class="border-b bg-white border-gray-200 dark:bg-gray-950 dark:border-gray-900">
        <div class="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">
            <RouterLink :to="{ name: 'Home' }" class="flex items-center space-x-3 rtl:space-x-reverse">
                <img src="/logo.svg" class="h-10" alt="Logviz Logo" />
                <span
                    class="self-center text-2xl font-semibold text-gray-900 dark:text-gray-300 hover:text-primary-600 hidden sm:flex">
                    Logviz
                </span>
            </RouterLink>
            <div class="flex md:order-2 space-x-3 md:space-x-0 rtl:space-x-reverse">
                <button type="button" @click="$router.push({ name: 'Solve' })"
                    class="mx-5 px-8 py-2 text-white bg-primary-400 hover:bg-primary-500 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">Solve</button>
                <button data-collapse-toggle="navbar-cta" type="button"
                    class="inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600"
                    aria-controls="navbar-cta" aria-expanded="false">
                    <span class="sr-only">Open main menu</span>
                    <svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none"
                        viewBox="0 0 17 14">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M1 1h15M1 7h15M1 13h15" />
                    </svg>
                </button>
                <button id="theme-toggle" type="button"
                    class="text-gray-900 dark:text-white hover:text-primary-600 p-2.5">
                    <svg id="theme-toggle-dark-icon" class="w-5 h-5 hidden" fill="currentColor" viewBox="0 0 24 24"
                        xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd"
                            d="M11.7 2a10 10 0 1 0 9.8 13.3 1 1 0 0 0-1-1.3H20a8 8 0 0 1-7.6-10.6l.1-.4a1 1 0 0 0-.8-1Z"
                            clip-rule="evenodd" />
                    </svg>

                    <svg id="theme-toggle-light-icon" class="w-5 h-5 hidden" fill="currentColor" viewBox="0 0 20 20"
                        xmlns="http://www.w3.org/2000/svg">
                        <path
                            d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z"
                            fill-rule="evenodd" clip-rule="evenodd"></path>
                    </svg>
                </button>
            </div>
            <div class="items-center justify-between hidden w-full md:flex md:w-auto md:order-1" id="navbar-cta">
                <ul
                    class="flex flex-col font-medium p-4 md:p-0 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:space-x-8 rtl:space-x-reverse md:flex-row md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-950 dark:border-gray-700">
                    <li>
                        <RouterLink to="/runs"
                            class="block py-2 px-3 md:p-0 text-gray-900 rounded hover:text-primary-600 md:hover:bg-transparent md:hover:text-primary md:dark:hover:text-primary-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700">
                            Runs</RouterLink>
                    </li>
                    <li>
                        <RouterLink to="/live"
                            class="block py-2 px-3 md:p-0 text-gray-900 rounded hover:text-primary-600 md:hover:bg-transparent md:hover:text-primary md:dark:hover:text-primary-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700">
                            Live Monitor</RouterLink>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</template>

<script setup lang="ts">

</script>

<style scoped></style>