from pydantic import BaseModel


class Defaults(BaseModel):
    totalAllocation: int
    rewardPerAllocation: int
    rewardPerReferral: int
    reservedAllocation: int


class Data(BaseModel):
    eligible: bool
    reserved: bool
    totalAllocated: int
    referralBonus: int
    noOfReferrals: int
    referralLink: str
    defaults: Defaults


class AidogsAllocationResponse(BaseModel):
    status: int
    message: str
    data: Data
