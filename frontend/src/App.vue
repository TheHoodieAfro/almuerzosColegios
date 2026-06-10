<script setup>
import { useRouter } from "vue-router";

const router = useRouter();
</script>

<template>
    <div class="min-h-screen bg-gray-50">
        <nav class="bg-white shadow-sm px-6 py-4 flex gap-6">
            <button
                @click="router.push('/')"
                class="text-gray-600 hover:text-blue-500 font-medium"
            >
                Registro
            </button>
            <button
                @click="router.push('/reports')"
                class="text-gray-600 hover:text-blue-500 font-medium"
            >
                Reportes
            </button>
        </nav>

        <RouterView />
    </div>
</template>
