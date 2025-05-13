import './App.css';
import {
  Tabs,
  TabsContent,
  TabsList,
  TabsTrigger,
} from './components/tabs.jsx';
import ClassicCalculator from './components/classic-calculator.jsx';
import MatrixCalculator from './components/matrix-calculator.jsx';
import { useState } from 'react';
import EquationCalculator from './components/equation-calculator.jsx';
import { Toaster } from './components/sonner.jsx';
import { cn } from './lib/utils.js';
import ClassicHelper from './components/classic-helper.jsx';
import EquationHelper from './components/equation-helper.jsx';
import MatrixHelper from './components/matrix-helper.jsx';

export default function App() {
  const [mode, setMode] = useState('classic');

  return (
    <>
      <div className="px-6 py-30 gap-20 grid grid-cols-2 bg-black/95 h-screen">
        <div className="border max-w-3xl h-fit w-full rounded-lg bg-white flex flex-col justify-start items-center p-4 shadow-xs">
          <div className="mb-6 flex justify-between items-center w-full">
            <h1 className="text-2xl font-semibold">Calculator Cucumber</h1>
            <div className="flex justify-end items-center">
              <button
                onClick={() => setMode('classic')}
                className={cn(
                  'bg-background text-black row-span-2 flex justify-center items-center px-3 py-2 rounded hover:bg-muted [&_svg]:size-4 disabled:text-gray-200 disabled:hover:text-muted',
                  mode === 'classic' && 'bg-muted',
                )}
              >
                Classic
              </button>
              <button
                onClick={() => setMode('equation')}
                className={cn(
                  'bg-background text-black row-span-2 flex justify-center items-center px-3 py-2 rounded hover:bg-muted [&_svg]:size-4 disabled:text-gray-200 disabled:hover:text-muted',
                  mode === 'equation' && 'bg-muted',
                )}
              >
                Equation Solver
              </button>
              <button
                onClick={() => setMode('matrix')}
                className={cn(
                  'bg-background text-black row-span-2 flex justify-center items-center px-3 py-2 rounded hover:bg-muted [&_svg]:size-4 disabled:text-gray-200 disabled:hover:text-muted',
                  mode === 'matrix' && 'bg-muted',
                )}
              >
                Matrix
              </button>
            </div>
          </div>

          {mode === 'classic' && <ClassicCalculator />}
          {mode === 'equation' && <EquationCalculator />}
          {mode === 'matrix' && <MatrixCalculator />}

          <p className="mt-3 text-xs text-muted-foreground/40">
            By Arsène Mujyabwami, Ingrid Fondja Tchoumba, Nicolas Delplanque and
            Xavier Delabie{' '}
          </p>
        </div>
        <div className="flex flex-col gap-6 justify-start items-start h-full w-full bg-white rounded-md p-4">
          <p className="text-lg font-medium">Helper</p>
          <Tabs
            defaultValue="tab-1"
            orientation="vertical"
            className="w-full h-full flex flex-row"
          >
            <TabsList className="flex-col justify-start rounded-none border-l h-fit bg-transparent p-0">
              <TabsTrigger
                value="tab-1"
                className="data-[state=active]:after:bg-primary relative w-full justify-start rounded-none after:absolute after:inset-y-0 after:start-0 after:w-0.5 data-[state=active]:bg-transparent data-[state=active]:shadow-none"
              >
                Classic
              </TabsTrigger>
              <TabsTrigger
                value="tab-2"
                className="data-[state=active]:after:bg-primary relative w-full justify-start rounded-none after:absolute after:inset-y-0 after:start-0 after:w-0.5 data-[state=active]:bg-transparent data-[state=active]:shadow-none"
              >
                Equation Solver
              </TabsTrigger>
              <TabsTrigger
                value="tab-3"
                className="data-[state=active]:after:bg-primary relative w-full justify-start rounded-none after:absolute after:inset-y-0 after:start-0 after:w-0.5 data-[state=active]:bg-transparent data-[state=active]:shadow-none"
              >
                Matrix
              </TabsTrigger>
            </TabsList>
            <div className="grow rounded-md border text-start">
              <TabsContent value="tab-1">
                <ClassicHelper />
              </TabsContent>
              <TabsContent value="tab-2">
                <EquationHelper />
              </TabsContent>
              <TabsContent value="tab-3">
                <MatrixHelper />
              </TabsContent>
            </div>
          </Tabs>
        </div>
      </div>
      <Toaster position="top-center" richColors />
    </>
  );
}
