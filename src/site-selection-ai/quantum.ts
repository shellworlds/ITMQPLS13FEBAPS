export interface QuantumResult {
    branch: string;
    energy: number;
}
export function compute(): QuantumResult {
    return { branch: "site-selection-ai", energy: Math.random() };
}
