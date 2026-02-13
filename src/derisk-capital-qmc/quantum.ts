export interface QuantumResult {
    branch: string;
    energy: number;
}
export function compute(): QuantumResult {
    return { branch: "derisk-capital-qmc", energy: Math.random() };
}
