import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Formulario de Contacto La Salle",
  description: "Actividad 4 — Ingeniería de Software, Universidad de La Salle",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="es">
      <body>{children}</body>
    </html>
  );
}
