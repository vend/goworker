package vetrics

import (
	"time"

	"github.com/rcrowley/go-metrics"
)

// WrappedTimer is a Timer with some convenience methods like .Start().End().
type WrappedTimer struct {
	underlying metrics.Timer
}

// WrappedTimerInvocation keeps track of the the start time for a particular invocation of a WrappedTimer. Only exists so you can call End().
type WrappedTimerInvocation struct {
	WrappedTimer
	StartTime time.Time
}

// Start returns a thing you can call .End() on.
func (wt WrappedTimer) Start() StartedTimer {
	return WrappedTimerInvocation{
		WrappedTimer: wt,
		StartTime:    time.Now(),
	}
}

// Update marks the duration of a given event. Useful when you can't use the Start().Stop() method which should be preferred.
func (wt WrappedTimer) Update(dur time.Duration) {
	wt.underlying.Update(dur)
}

// UpdateSince marks an event as having started at since, and finished now
func (wt WrappedTimer) UpdateSince(since time.Time) {
	wt.underlying.UpdateSince(since)
}

// End completes the timer invocation started with Start().
func (wti WrappedTimerInvocation) Stop() {
	duration := time.Since(wti.StartTime)
	wti.WrappedTimer.underlying.Update(duration)
}
