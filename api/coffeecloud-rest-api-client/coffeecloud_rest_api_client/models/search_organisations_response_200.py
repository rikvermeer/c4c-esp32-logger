from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchOrganisationsResponse200")


@attr.s(auto_attribs=True)
class SearchOrganisationsResponse200:
    """
    Attributes:
        page (Union[Unset, int]):
        amount_of_pages (Union[Unset, int]):
        items (Union[Unset, List[Any]]):
    """

    page: Union[Unset, int] = UNSET
    amount_of_pages: Union[Unset, int] = UNSET
    items: Union[Unset, List[Any]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        page = self.page
        amount_of_pages = self.amount_of_pages
        items: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data

                items.append(items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if page is not UNSET:
            field_dict["page"] = page
        if amount_of_pages is not UNSET:
            field_dict["amount_of_pages"] = amount_of_pages
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        page = d.pop("page", UNSET)

        amount_of_pages = d.pop("amount_of_pages", UNSET)

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = items_item_data

            items.append(items_item)

        search_organisations_response_200 = cls(
            page=page,
            amount_of_pages=amount_of_pages,
            items=items,
        )

        search_organisations_response_200.additional_properties = d
        return search_organisations_response_200

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
