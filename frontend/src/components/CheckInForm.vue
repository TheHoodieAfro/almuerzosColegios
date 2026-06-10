<script setup>
import { ref } from "vue";

const emit = defineEmits(["submit"]);
const colegioId = ref("");

function handleSubmit() {
    if (!colegioId.value) return;
    emit("submit", colegioId.value); // just tells the parent "user submitted this ID"
    colegioId.value = "";
}
</script>

<template>
    <div class="flex flex-col items-center gap-4 p-6">
        <input
            v-model="colegioId"
            type="text"
            placeholder="Ingresa tu codigo de estudiante"
            @keyup.enter="handleSubmit"
            class="border rounded-lg px-4 py-2 w-full max-w-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        <button
            @click="handleSubmit"
            class="bg-blue-500 hover:bg-blue-600 text-white font-semibold px-6 py-2 rounded-lg w-full max-w-sm"
        >
            Registrar Asistencia
        </button>
        <p v-if="message" :class="isError ? 'text-red-500' : 'text-green-500'">
            {{ message }}
        </p>
    </div>
</template>
