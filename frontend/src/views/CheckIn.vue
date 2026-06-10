<script setup>
import { ref } from "vue";
import { postCheckIn } from "../services/API.js";
import CheckInForm from "../components/CheckInForm.vue";

const message = ref("");
const isError = ref(false);

async function handleCheckIn(colegioId) {
    try {
        await postCheckIn(colegioId);
        message.value = "Asistencia registrada exitosamente";
        isError.value = false;
    } catch (error) {
        message.value = error.message;
        isError.value = true;
    }
}
</script>

<template>
    <div
        class="flex flex-col items-center justify-center bg-gray-50 p-6"
        style="height: calc(100vh - 300px)"
    >
        <div
            class="bg-white rounded-xl shadow-md p-8 w-full max-w-md flex flex-col justify-start min-h-80"
        >
            <h1 class="text-2xl font-bold text-gray-700 text-center mb-6">
                Registro de Almuerzo
            </h1>
            <CheckInForm @submit="handleCheckIn" />
            <p
                v-if="message"
                :class="isError ? 'text-red-500' : 'text-green-500'"
                class="text-center mt-4"
            >
                {{ message }}
            </p>
        </div>
    </div>
</template>
