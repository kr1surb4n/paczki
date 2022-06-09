/** @type {import('ts-jest/dist/types').InitialOptionsTsJest} */
import type { Config } from "@jest/types"

const config: Config.InitialOptions = {
  preset: "ts-jest",
  // testEnvironment: "node",
  testEnvironment: "jsdom",
  testMatch: [ "**/__tests__/**/*.[jt]s?(x)", "**/?(*.)+(test).[jt]s?(x)" ],
  verbose: true,
  // automock: true,
  moduleNameMapper: {
    "@/(.*)$": "<rootDir>/resources/js/$1"
  }
}
export default config