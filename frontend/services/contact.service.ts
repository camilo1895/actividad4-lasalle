import { request } from "@/lib/api"; // ajusta la ruta según tu proyecto

type ContactoForm = {
  nombre: string;
  correo: string;
  asunto: string;
  mensaje: string;
};

export async function enviarContacto(data: ContactoForm) {
  return request<{ message: string }>("/api/v1/contactos", {
    method: "POST",
    body: data,
  });
}
