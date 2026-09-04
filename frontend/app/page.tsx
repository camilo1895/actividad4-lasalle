import ContactForm from "@/components/ContactForm";

export default function Home() {
  const env = process.env.NEXT_PUBLIC_APP_ENV;
  const mostrarBadge = process.env.NEXT_PUBLIC_SHOW_ENV_BADGE === "true";

  return (
    <main className="min-h-screen bg-gray-50 flex items-center justify-center px-6 py-10">
      <div className="w-full max-w-lg bg-white shadow-lg rounded-lg p-8">
        {mostrarBadge && env && (
          <div className="flex items-center justify-end">
            <span className="text-xs uppercase rounded-full bg-blue-100 text-blue-700 px-3 py-1 font-semibold shadow-sm">
              {env}
            </span>
          </div>
        )}

        <div className="flex items-center justify-between my-4">
          <h1 className="text-2xl font-semibold">
            Formulario de Contacto La Salle
          </h1>
        </div>
        <ContactForm />
      </div>
    </main>
  );
}
