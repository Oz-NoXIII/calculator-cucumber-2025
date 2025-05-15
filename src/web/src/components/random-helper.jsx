export default function RandomHelper() {
  return (
    <div className="py-1.5 px-4 h-full flex flex-col justify-between">
      <div className="grid gap-6 grid-cols-1">
        <div className="flex flex-col gap-3">
          <p className="text-muted-foreground text-xs">
            How do I calculate random integer?
          </p>
          <div className="grid pl-4 text-sm">
            <p>
              Press the Random Integer button to get the random integer
              generated.
            </p>
          </div>
        </div>
        <div className="flex flex-col gap-3">
          <p className="text-muted-foreground text-xs">
            How do I calculate random rational?
          </p>
          <div className="grid pl-4 text-sm">
            <p>
              Press the Random Rational button to get the random rational
              generated.
            </p>
          </div>
        </div>
        <div className="flex flex-col gap-3">
          <p className="text-muted-foreground text-xs">
            How do I calculate random complex?
          </p>
          <div className="grid pl-4 text-sm">
            <p>
              Press the Random Complex button to get the random complex
              generated.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}
