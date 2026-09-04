"use client";

import { useState, type FormEvent } from "react";
import type { ContactoForm } from "@/types/contacto";
import { enviarContacto } from "@/services/contact.service";

const LIMITES = {
  nombre: 100,
  correo: 254,
  asunto: 150,
  mensaje: 2000,
} as const;

const EMAIL_REGEX = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

type Campo = keyof ContactoForm;
type Errores = Partial<Record<Campo, string>>;

const initialForm: ContactoForm = {
  nombre: "",
  correo: "",
  asunto: "",
  mensaje: "",
};

function esSoloEspacios(valor: string): boolean {
  return valor.trim().length === 0;
}

function validarCampo(campo: Campo, valor: string): string | undefined {
  if (esSoloEspacios(valor)) {
    return "Este campo es obligatorio.";
  }
  if (valor.length > LIMITES[campo]) {
    return `Máximo ${LIMITES[campo]} caracteres.`;
  }
  if (campo === "correo" && !EMAIL_REGEX.test(valor.trim())) {
    return "Ingresa un correo electrónico válido.";
  }
  return undefined;
}

function validarFormulario(form: ContactoForm): Errores {
  const errores: Errores = {};
  (Object.keys(form) as Campo[]).forEach((campo) => {
    const error = validarCampo(campo, form[campo]);
    if (error) errores[campo] = error;
  });
  return errores;
}

export default function ContactForm() {
  const [form, setForm] = useState<ContactoForm>(initialForm);
  const [errores, setErrores] = useState<Errores>({});
  const [enviando, setEnviando] = useState(false);
  const [confirmacion, setConfirmacion] = useState<string | null>(null);
  const [errorServidor, setErrorServidor] = useState<string | null>(null);

  const handleChange =
    (campo: Campo) =>
    (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
      const valor = e.target.value;
      setForm((prev) => ({ ...prev, [campo]: valor }));
      setErrores((prev) => ({ ...prev, [campo]: validarCampo(campo, valor) }));
    };

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    setConfirmacion(null);
    setErrorServidor(null);

    const erroresActuales = validarFormulario(form);
    setErrores(erroresActuales);
    if (Object.keys(erroresActuales).length > 0) {
      return;
    }

    setEnviando(true);
    try {
      const resultado = await enviarContacto({
        nombre: form.nombre.trim(),
        correo: form.correo.trim(),
        asunto: form.asunto.trim(),
        mensaje: form.mensaje.trim(),
      });

      if (resultado.ok) {
        setConfirmacion("Mensaje enviado correctamente.");
        setForm(initialForm);
      } else if (resultado.status === 422) {
        setErrorServidor(
          "Revisa los campos: el servidor rechazó los datos enviados.",
        );
      } else {
        setErrorServidor("No fue posible enviar el mensaje. Intenta de nuevo.");
      }
    } catch {
      setErrorServidor("No fue posible conectar con el servidor.");
    } finally {
      setEnviando(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} noValidate className="space-y-5 max-w-md">
      <div>
        <label htmlFor="nombre" className="block text-sm font-medium mb-1">
          Nombre
        </label>
        <input
          id="nombre"
          type="text"
          value={form.nombre}
          onChange={handleChange("nombre")}
          maxLength={LIMITES.nombre + 20}
          aria-invalid={Boolean(errores.nombre)}
          aria-describedby="nombre-error"
          className="w-full rounded border border-gray-300 px-3 py-2"
        />
        {errores.nombre && (
          <p id="nombre-error" className="text-sm text-red-600 mt-1">
            {errores.nombre}
          </p>
        )}
      </div>

      <div>
        <label htmlFor="correo" className="block text-sm font-medium mb-1">
          Correo electrónico
        </label>
        <input
          id="correo"
          type="email"
          value={form.correo}
          onChange={handleChange("correo")}
          maxLength={LIMITES.correo + 20}
          aria-invalid={Boolean(errores.correo)}
          aria-describedby="correo-error"
          className="w-full rounded border border-gray-300 px-3 py-2"
        />
        {errores.correo && (
          <p id="correo-error" className="text-sm text-red-600 mt-1">
            {errores.correo}
          </p>
        )}
      </div>

      <div>
        <label htmlFor="asunto" className="block text-sm font-medium mb-1">
          Asunto
        </label>
        <input
          id="asunto"
          type="text"
          value={form.asunto}
          onChange={handleChange("asunto")}
          maxLength={LIMITES.asunto + 20}
          aria-invalid={Boolean(errores.asunto)}
          aria-describedby="asunto-error"
          className="w-full rounded border border-gray-300 px-3 py-2"
        />
        {errores.asunto && (
          <p id="asunto-error" className="text-sm text-red-600 mt-1">
            {errores.asunto}
          </p>
        )}
      </div>

      <div>
        <label htmlFor="mensaje" className="block text-sm font-medium mb-1">
          Mensaje
        </label>
        <textarea
          id="mensaje"
          value={form.mensaje}
          onChange={handleChange("mensaje")}
          maxLength={LIMITES.mensaje + 20}
          rows={5}
          aria-invalid={Boolean(errores.mensaje)}
          aria-describedby="mensaje-error"
          className="w-full rounded border border-gray-300 px-3 py-2"
        />
        {errores.mensaje && (
          <p id="mensaje-error" className="text-sm text-red-600 mt-1">
            {errores.mensaje}
          </p>
        )}
      </div>

      <button
        type="submit"
        disabled={enviando}
        className="rounded bg-blue-600 px-4 py-2 text-white disabled:opacity-50"
      >
        {enviando ? "Enviando..." : "Enviar"}
      </button>

      {confirmacion && (
        <p role="status" className="text-sm text-green-700">
          {confirmacion}
        </p>
      )}
      {errorServidor && (
        <p role="alert" className="text-sm text-red-600">
          {errorServidor}
        </p>
      )}
    </form>
  );
}
