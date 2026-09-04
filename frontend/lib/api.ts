type ApiOptions = {
  method?: "GET" | "POST" | "PUT" | "PATCH" | "DELETE";
  body?: unknown;
};

export async function request<T>(
  path: string,
  options: ApiOptions = {},
): Promise<T> {
  const appEnv = process.env.APP_ENV;

  if (!appEnv) {
    throw new Error("Falta configurar APP_ENV");
  }

  if (
    appEnv !== "development" &&
    appEnv !== "test" &&
    appEnv !== "production"
  ) {
    throw new Error("APP_ENV debe ser development, test o production");
  }

  const baseUrls = {
    development: process.env.DEV_NEXT_PUBLIC_API_BASE_URL,
    test: process.env.TEST_NEXT_PUBLIC_API_BASE_URL,
    production: process.env.PROD_NEXT_PUBLIC_API_BASE_URL,
  };

  const baseUrl = baseUrls[appEnv];

  if (!baseUrl) {
    throw new Error(`Falta configurar la URL de la API para ${appEnv}`);
  }

  const method = options.method ?? "GET";
  const hasBody = options.body !== undefined;
  const headers: Record<string, string> = {
    Accept: "application/json",
  };

  if (hasBody) {
    headers["Content-Type"] = "application/json";
  }

  if (method === "GET" && hasBody) {
    throw new Error("Las consultas GET no deben enviar body");
  }

  const response = await fetch(`${baseUrl}${path}`, {
    method,
    headers,
    body: hasBody ? JSON.stringify(options.body) : undefined,
    cache: "no-store",
    signal: AbortSignal.timeout(8000),
  });

  if (!response.ok) {
    throw new Error(`La API respondió con HTTP ${response.status}`);
  }

  return response.json();
}
