import {
  Tabs,
  TabsContent,
  TabsList,
  TabsTrigger,
} from './components/tabs.jsx';
import ClassicCalculator from './components/classic-calculator.jsx';
import MatrixCalculator from './components/matrix-calculator.jsx';

export default function App() {
  const [mode, setMode] = useState('classic');

  return (
    <div className="px-6 py-30 gap-20 grid grid-cols-2 bg-black/95 h-screen">
      <div className="border max-w-3xl h-fit w-full rounded-lg bg-white flex flex-col justify-start items-center p-4 shadow-xs">
        <div className="mb-6 flex justify-between items-center w-full">
          <h1 className="text-2xl font-semibold">Calculator Cucumber</h1>
          <div className="flex justify-end items-center">
            <button
              onClick={() => setMode('classic')}
              className="bg-background text-black row-span-2 flex justify-center items-center px-3 py-2 rounded hover:bg-muted [&_svg]:size-4 disabled:text-gray-200 disabled:hover:text-muted"
            >
              Classic
            </button>
            <button
              onClick={() => setMode('matrix')}
              className="bg-background text-black row-span-2 flex justify-center items-center px-3 py-2 rounded hover:bg-muted [&_svg]:size-4 disabled:text-gray-200 disabled:hover:text-muted"
            >
              Matrix
            </button>
          </div>
        </div>

        {mode === 'classic' && <ClassicCalculator />}
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
              Matrix
            </TabsTrigger>
            <TabsTrigger
              value="tab-3"
              className="data-[state=active]:after:bg-primary relative w-full justify-start rounded-none after:absolute after:inset-y-0 after:start-0 after:w-0.5 data-[state=active]:bg-transparent data-[state=active]:shadow-none"
            >
              ?
            </TabsTrigger>
          </TabsList>
          <div className="grow rounded-md border text-start">
            <TabsContent
              value="tab-1"
              className="py-3 px-4 grid gap-3 grid-cols-2"
            >
              <div className="flex flex-col gap-3">
                <p className="text-muted-foreground text-xs">Infix</p>
                <div className="grid pl-4 text-sm">
                  <p>
                    <span className="font-bold">Addition :</span> a + b
                  </p>
                  <p>
                    <span className="font-bold">Subtraction :</span> a - b
                  </p>
                  <p>
                    <span className="font-bold">Multiplication :</span> a * b
                  </p>
                  <p>
                    <span className="font-bold">Division :</span> a / b
                  </p>
                  <p>
                    <span className="font-bold">Exponentiation :</span> a ^ b
                  </p>
                  <p>
                    <span className="font-bold">Negation :</span> (-a)
                  </p>
                  <p>
                    <span className="font-bold">Inverse :</span> inv(a)
                  </p>
                </div>
              </div>
              <div className="flex flex-col gap-3">
                <p className="text-muted-foreground text-xs">Prefix</p>
                <div className="grid pl-4 text-sm">
                  <p>
                    <span className="font-bold">Addition :</span> +(a, b){' '}
                    <span className="text-muted-foreground/60 font-medium text-xs">
                      or
                    </span>{' '}
                    +(a b)
                  </p>
                  <p>
                    <span className="font-bold">Subtraction :</span> -(a, b){' '}
                    <span className="text-muted-foreground/60 font-medium text-xs">
                      or
                    </span>{' '}
                    -(a b)
                  </p>
                  <p>
                    <span className="font-bold">Multiplication :</span> *(a, b){' '}
                    <span className="text-muted-foreground/60 font-medium text-xs">
                      or
                    </span>{' '}
                    *(a b)
                  </p>
                  <p>
                    <span className="font-bold">Division :</span> /(a, b){' '}
                    <span className="text-muted-foreground/60 font-medium text-xs">
                      or
                    </span>{' '}
                    /(a b)
                  </p>
                  <p>
                    <span className="font-bold">Exponentiation :</span> ^(a, b){' '}
                    <span className="text-muted-foreground/60 font-medium text-xs">
                      or
                    </span>{' '}
                    ^(a b)
                  </p>
                  <p>
                    <span className="font-bold">Negation :</span> (-(a))
                  </p>
                  <p>
                    <span className="font-bold">Inverse :</span> inv(a)
                  </p>
                </div>
              </div>
              <div className="flex flex-col gap-3">
                <p className="text-muted-foreground text-xs">Postfix</p>
                <div className="grid pl-4 text-sm">
                  <p>
                    <span className="font-bold">Addition :</span> (a, b)+{' '}
                    <span className="text-muted-foreground/60 font-medium text-xs">
                      or
                    </span>{' '}
                    (a b)+
                  </p>
                  <p>
                    <span className="font-bold">Subtraction :</span> (a, b)-{' '}
                    <span className="text-muted-foreground/60 font-medium text-xs">
                      or
                    </span>{' '}
                    (a b)-
                  </p>
                  <p>
                    <span className="font-bold">Multiplication :</span> (a, b)*{' '}
                    <span className="text-muted-foreground/60 font-medium text-xs">
                      or
                    </span>{' '}
                    (a b)*
                  </p>
                  <p>
                    <span className="font-bold">Division :</span> (a, b)/{' '}
                    <span className="text-muted-foreground/60 font-medium text-xs">
                      or
                    </span>{' '}
                    (a b)/
                  </p>
                  <p>
                    <span className="font-bold">Exponentiation :</span> (a, b)^{' '}
                    <span className="text-muted-foreground/60 font-medium text-xs">
                      or
                    </span>{' '}
                    (a b)^
                  </p>
                  <p>
                    <span className="font-bold">Negation :</span> (a-)-
                  </p>
                  <p>
                    <span className="font-bold">Inverse :</span> inv(a)
                  </p>
                </div>
              </div>
              <div className="flex flex-col gap-3">
                <p className="text-muted-foreground text-xs">Others</p>
                <div className="grid pl-4 text-sm">
                  <p>
                    <span className="font-bold">Multiple operands :</span> +(a,
                    b, c)
                  </p>
                  <p>
                    <span className="font-bold">Nested operations :</span> *(a,
                    +(b, c))
                  </p>
                  <p>
                    <span className="font-bold">Complex numbers :</span> a + bj
                  </p>
                  <p>
                    <span className="font-bold">Parentheses :</span> (a + b) * c
                  </p>
                </div>
              </div>
            </TabsContent>
            <TabsContent value="tab-2">
              <p className="text-muted-foreground px-4 py-3 text-xs">
                Content for Tab 2
              </p>
            </TabsContent>
            <TabsContent value="tab-3">
              <p className="text-muted-foreground px-4 py-3 text-xs">
                Content for Tab 3
              </p>
            </TabsContent>
          </div>
        </Tabs>
      </div>
    </div>
  );
}
