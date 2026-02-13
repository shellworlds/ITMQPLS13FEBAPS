export interface QuantumResult {
    branch: string;
    energy: number;
}
export function compute(): QuantumResult {
    return { branch: "project-finance-2.0", energy: Math.random() };
}
