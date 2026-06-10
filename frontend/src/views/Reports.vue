<script setup>
import { ref } from "vue";
import { getRecords } from "../services/API.js";
import RecordsTable from "../components/RecordsTable.vue";

const start = ref("");
const end = ref("");
const report = ref(null); // null means no report loaded yet
const isError = ref(false);
const message = ref("");

async function handleSearch() {
    if (!start.value || !end.value) {
        message.value = "Por favor seleccionar ambas fechas";
        isError.value = true;
        return;
    }

    if (end.value < start.value) {
        message.value = "La fecha de fin debe ser depues a la fecha de inicio";
        isError.value = true;
        return;
    }

    try {
        report.value = await getRecords(start.value, end.value);
        message.value = "";
        isError.value = false;
    } catch (error) {
        message.value = error.message;
        isError.value = true;
        report.value = null;
    }
}
</script>

<template>
    <div class="bg-gray-50 p-6">
        <div class="max-w-4xl mx-auto">
            <h1 class="text-2xl font-bold text-gray-700 mb-6">
                Reporte de Asistencias
            </h1>

            <div class="bg-white rounded-xl shadow-md p-6 mb-6">
                <div class="flex flex-col sm:flex-row gap-4 items-end">
                    <div class="flex flex-col gap-1 w-full">
                        <label class="text-sm text-gray-500">Desde</label>
                        <input
                            v-model="start"
                            type="date"
                            class="border rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
                        />
                    </div>
                    <div class="flex flex-col gap-1 w-full">
                        <label class="text-sm text-gray-500">Hasta</label>
                        <input
                            v-model="end"
                            type="date"
                            class="border rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
                        />
                    </div>
                    <button
                        @click="handleSearch"
                        class="bg-blue-500 hover:bg-blue-600 text-white font-semibold px-6 py-2 rounded-lg whitespace-nowrap"
                    >
                        Buscar
                    </button>
                </div>

                <p
                    v-if="message"
                    :class="isError ? 'text-red-500' : 'text-green-500'"
                    class="mt-3 text-sm"
                >
                    {{ message }}
                </p>
            </div>

            <div v-if="report" class="bg-white rounded-xl shadow-md p-6">
                <RecordsTable
                    :records="report.records"
                    :total="report.total"
                    :start="start"
                    :end="end"
                />
            </div>
        </div>
    </div>
</template>
