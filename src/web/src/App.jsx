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
import ScientificHelper from './components/scientific-helper.jsx';
import RandomCalculator from './components/random-calculator.jsx';
import ScientificCalculator from './components/scientific-calculator.jsx';
import RandomHelper from './components/random-helper.jsx';

export default function App() {
  const [tab, setTab] = useState('classic');
  const [mode, setMode] = useState('classic');

  return (
    <>
      <div className="px-6 py-6 bg-black/95 h-screen overflow-hidden">
        <h1 className="text-4xl text-center text-white font-semibold">
          Calculator Cucumber
        </h1>
        <div className="px-6 py-24 gap-20 grid grid-cols-2 items-stretch">
          <div className="border max-w-3xl h-[600px] w-full rounded-lg bg-white flex flex-col justify-start items-center p-4 shadow-xs">
            <div className="mb-6 flex justify-center items-center w-full">
              <div className="flex justify-end items-center gap-1">
                <button
                  onClick={() => {
                    setMode('classic');
                    setTab('classic');
                  }}
                  className={cn(
                    'bg-background text-black row-span-2 flex justify-center items-center px-3 py-2 rounded hover:bg-muted [&_svg]:size-4 disabled:text-gray-200 disabled:hover:text-muted',
                    mode === 'classic' && 'bg-muted',
                  )}
                >
                  Classic
                </button>
                <button
                  onClick={() => {
                    setMode('scientific');
                    setTab('scientific');
                  }}
                  className={cn(
                    'bg-background text-black row-span-2 flex justify-center items-center px-3 py-2 rounded hover:bg-muted [&_svg]:size-4 disabled:text-gray-200 disabled:hover:text-muted',
                    mode === 'scientific' && 'bg-muted',
                  )}
                >
                  Scientific
                </button>
                <button
                  onClick={() => {
                    setMode('equation');
                    setTab('equation');
                  }}
                  className={cn(
                    'bg-background text-black row-span-2 flex justify-center items-center px-3 py-2 rounded hover:bg-muted [&_svg]:size-4 disabled:text-gray-200 disabled:hover:text-muted',
                    mode === 'equation' && 'bg-muted',
                  )}
                >
                  Equation Solver
                </button>
                <button
                  onClick={() => {
                    setMode('matrix');
                    setTab('matrix');
                  }}
                  className={cn(
                    'bg-background text-black row-span-2 flex justify-center items-center px-3 py-2 rounded hover:bg-muted [&_svg]:size-4 disabled:text-gray-200 disabled:hover:text-muted',
                    mode === 'matrix' && 'bg-muted',
                  )}
                >
                  Matrix
                </button>
                <button
                  onClick={() => {
                    setMode('random');
                    setTab('random');
                  }}
                  className={cn(
                    'bg-background text-black row-span-2 flex justify-center items-center px-3 py-2 rounded hover:bg-muted [&_svg]:size-4 disabled:text-gray-200 disabled:hover:text-muted',
                    mode === 'random' && 'bg-muted',
                  )}
                >
                  Random
                </button>
              </div>
            </div>

            {mode === 'classic' && <ClassicCalculator />}
            {mode === 'scientific' && <ScientificCalculator />}
            {mode === 'equation' && <EquationCalculator />}
            {mode === 'matrix' && <MatrixCalculator />}
            {mode === 'random' && <RandomCalculator />}

            <p className="mt-auto text-xs text-muted-foreground/40">
              By Arsène Mujyabwami, Ingrid Fondja Tchoumba, Nicolas Delplanque
              and Xavier Delabie{' '}
            </p>
          </div>
          <div className="flex flex-col gap-6 justify-start items-start h-[600px] w-full bg-white rounded-md p-4">
            <p className="text-lg font-medium">Helper</p>
            <Tabs
              defaultValue={tab}
              value={tab}
              onValueChange={(value) => setTab(value)}
              className="w-full h-full flex"
            >
              <TabsList className="flex justify-start rounded-none h-fit bg-transparent p-0">
                <TabsTrigger
                  value="classic"
                  className="data-[state=active]:after:bg-primary relative rounded-none py-2 after:absolute after:inset-x-0 after:bottom-0 after:h-0.5 data-[state=active]:bg-transparent data-[state=active]:shadow-none"
                >
                  Classic
                </TabsTrigger>
                <TabsTrigger
                  value="scientific"
                  className="data-[state=active]:after:bg-primary relative rounded-none py-2 after:absolute after:inset-x-0 after:bottom-0 after:h-0.5 data-[state=active]:bg-transparent data-[state=active]:shadow-none"
                >
                  Scientific
                </TabsTrigger>
                <TabsTrigger
                  value="equation"
                  className="data-[state=active]:after:bg-primary relative rounded-none py-2 after:absolute after:inset-x-0 after:bottom-0 after:h-0.5 data-[state=active]:bg-transparent data-[state=active]:shadow-none"
                >
                  Equation Solver
                </TabsTrigger>
                <TabsTrigger
                  value="matrix"
                  className="data-[state=active]:after:bg-primary relative rounded-none py-2 after:absolute after:inset-x-0 after:bottom-0 after:h-0.5 data-[state=active]:bg-transparent data-[state=active]:shadow-none"
                >
                  Matrix
                </TabsTrigger>
                <TabsTrigger
                  value="random"
                  className="data-[state=active]:after:bg-primary relative rounded-none py-2 after:absolute after:inset-x-0 after:bottom-0 after:h-0.5 data-[state=active]:bg-transparent data-[state=active]:shadow-none"
                >
                  Random
                </TabsTrigger>
              </TabsList>
              <TabsContent value="classic">
                <ClassicHelper />
              </TabsContent>
              <TabsContent value="scientific">
                <ScientificHelper />
              </TabsContent>
              <TabsContent value="equation">
                <EquationHelper />
              </TabsContent>
              <TabsContent value="matrix">
                <MatrixHelper />
              </TabsContent>
              <TabsContent value="random">
                <RandomHelper />
              </TabsContent>
            </Tabs>
          </div>
        </div>
      </div>
      <Toaster position="top-center" richColors />
    </>
  );
}
