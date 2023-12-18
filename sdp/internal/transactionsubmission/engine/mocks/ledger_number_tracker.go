// Code generated by mockery v2.27.1. DO NOT EDIT.

package mocks

import (
	txnbuild "github.com/stellar/go/txnbuild"
	mock "github.com/stretchr/testify/mock"
)

// MockLedgerNumberTracker is an autogenerated mock type for the LedgerNumberTracker type
type MockLedgerNumberTracker struct {
	mock.Mock
}

// GetLedgerBounds provides a mock function with given fields:
func (_m *MockLedgerNumberTracker) GetLedgerBounds() (*txnbuild.LedgerBounds, error) {
	ret := _m.Called()

	var r0 *txnbuild.LedgerBounds
	var r1 error
	if rf, ok := ret.Get(0).(func() (*txnbuild.LedgerBounds, error)); ok {
		return rf()
	}
	if rf, ok := ret.Get(0).(func() *txnbuild.LedgerBounds); ok {
		r0 = rf()
	} else {
		if ret.Get(0) != nil {
			r0 = ret.Get(0).(*txnbuild.LedgerBounds)
		}
	}

	if rf, ok := ret.Get(1).(func() error); ok {
		r1 = rf()
	} else {
		r1 = ret.Error(1)
	}

	return r0, r1
}

// GetLedgerNumber provides a mock function with given fields:
func (_m *MockLedgerNumberTracker) GetLedgerNumber() (int, error) {
	ret := _m.Called()

	var r0 int
	var r1 error
	if rf, ok := ret.Get(0).(func() (int, error)); ok {
		return rf()
	}
	if rf, ok := ret.Get(0).(func() int); ok {
		r0 = rf()
	} else {
		r0 = ret.Get(0).(int)
	}

	if rf, ok := ret.Get(1).(func() error); ok {
		r1 = rf()
	} else {
		r1 = ret.Error(1)
	}

	return r0, r1
}

type mockConstructorTestingTNewMockLedgerNumberTracker interface {
	mock.TestingT
	Cleanup(func())
}

// NewMockLedgerNumberTracker creates a new instance of MockLedgerNumberTracker. It also registers a testing interface on the mock and a cleanup function to assert the mocks expectations.
func NewMockLedgerNumberTracker(t mockConstructorTestingTNewMockLedgerNumberTracker) *MockLedgerNumberTracker {
	mock := &MockLedgerNumberTracker{}
	mock.Mock.Test(t)

	t.Cleanup(func() { mock.AssertExpectations(t) })

	return mock
}
