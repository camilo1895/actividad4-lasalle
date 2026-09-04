import { request } from "@/lib/api";
import type { ContactoForm } from "@/types/contacto";

type ContactoResponse = {
  id: number;
  message: string;
};

export function enviarContacto(data: ContactoForm) {
  return request<ContactoResponse>("/api/v1/contactos", {
    method: "POST",
    body: data,
  });
}
