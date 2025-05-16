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
              <span className="font-bold">1 :</span> Press the Random button.
            </p>
            <p>
              <span className="font-bold">2 :</span> Put an integer between
              brackets.{' '}
            </p>
            <p>
              <span className="font-bold">3 :</span> Press the equals (=) button
              to get the solution.
            </p>
            <p className="text-xs text-muted-foreground">
              e.g. rand(8) = random number between 0 and 8
            </p>
          </div>
        </div>
        <div className="flex flex-col gap-3">
          <p className="text-muted-foreground text-xs">
            How do I calculate random rational?
          </p>
          <div className="grid pl-4 text-sm">
            <p>
              <span className="font-bold">1 :</span> Press the Random button.
            </p>
            <p>
              <span className="font-bold">2 :</span> Put an rational number
              between brackets.{' '}
            </p>
            <p>
              <span className="font-bold">3 :</span> Press the equals (=) button
              to get the solution.
            </p>
            <p className="text-xs text-muted-foreground">
              e.g. rand(12.97) = random rational number between 0 and 1
            </p>
          </div>
        </div>
        <div className="flex flex-col gap-3">
          <p className="text-muted-foreground text-xs">
            How do I calculate random complex?
          </p>
          <div className="grid pl-4 text-sm">
            <p>
              <span className="font-bold">1 :</span> Press the Random button.
            </p>
            <p>
              <span className="font-bold">2 :</span> Put an complex number
              between brackets.{' '}
            </p>
            <p>
              <span className="font-bold">3 :</span> Press the equals (=) button
              to get the solution.
            </p>
            <p className="text-xs text-muted-foreground">
              e.g. rand(6j) = random complex number [between 0 and 1] + [between
              0 and 1]j
            </p>
          </div>
        </div>
      </div>
      <div className="flex flex-col col-span-2 gap-3">
        <p className="text-muted-foreground text-xs">Notes</p>
        <p className="text-sm text-orange-600">
          The result type matches the input : integers yield integers, rationals
          yield rationals, and complex inputs yield complex results.
        </p>
      </div>
    </div>
  );
}
