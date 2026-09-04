type ApiOptions = {
  method?: "GET" | "POST" | "PUT" | "PATCH" | "DELETE";
  body?: unknown;
};

export class ApiError extends Error {
  constructor(
    public readonly status: number,
    public readonly payload: unknown,
  ) {
    super(`La API respondió con HTTP ${status}`);
    this.name = "ApiError";
  }
}

export async function request<T>(
  path: string,
  options: ApiOptions = {},
): Promise<T> {
  const appEnv = process.env.NEXT_PUBLIC_APP_ENV;

  if (!appEnv) {
    throw new Error("Falta configurar NEXT_PUBLIC_APP_ENV");
  }

  if (
    appEnv !== "development" &&
    appEnv !== "test" &&
    appEnv !== "production"
  ) {
    throw new Error("APP_ENV debe ser development, test o production");
  }

  const baseUrls = {
    development: process.env.NEXT_PUBLIC_DEV_API_BASE_URL,
    test: process.env.NEXT_PUBLIC_TEST_API_BASE_URL,
    production: process.env.NEXT_PUBLIC_PROD_API_BASE_URL,
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

  const payload = await response.json().catch(() => null);

  if (!response.ok) {
    throw new ApiError(response.status, payload);
  }

  return payload as T;
}
