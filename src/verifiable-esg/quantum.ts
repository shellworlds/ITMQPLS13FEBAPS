export interface QuantumResult {
    branch: string;
    energy: number;
}
export function compute(): QuantumResult {
    return { branch: "verifiable-esg", energy: Math.random() };
}
